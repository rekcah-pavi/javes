# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for executing code and terminal commands from Telegram. """

import asyncio
import ast
import contextlib
from getpass import getuser
from os import remove
from sys import executable
from io import StringIO
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.eval(?:\s+([\S\s]+)|$)")
async def evaluate(query):
    """ For .eval command, evaluates the given Python expression. """
    reply = await query.get_reply_message()
    if query.is_channel and not query.is_group:
        await query.edit("`Eval isn't permitted on channels`")
        return

    if query.pattern_match.group(1):
        expression = query.pattern_match.group(1)
    elif reply:
        expression = reply
    else:
        await query.edit("``` Give an expression to evaluate. ```")
        return

    if expression in ("userbot.session", "config.env"):
        await query.edit("`That's a dangerous operation! Not Permitted!`")
        return

    try:
        response, out = await async_eval(expression,
                                         bot=bot,
                                         event=query,
                                         reply=reply)
        evaluation = str(response)
        if evaluation:
            if isinstance(evaluation, str):
                if len(evaluation) >= 4096:
                    file = open("output.txt", "w+")
                    file.write(evaluation)
                    file.close()
                    await query.client.send_file(
                        query.chat_id,
                        "output.txt",
                        reply_to=query.id,
                        caption="`Output too large, sending as file`",
                    )
                    remove("output.txt")
                    return
                await query.edit("**Query: **\n`"
                                 f"{expression}"
                                 "`\n**Result: **\n`"
                                 f"{evaluation}"
                                 "`")
        else:
            await query.edit("**Query: **\n`"
                             f"{expression}"
                             "`\n**Result: **\n`No Result Returned/False`")
    except Exception as err:
        await query.edit("**Query: **\n`"
                         f"{expression}"
                         "`\n**Exception: **\n"
                         f"`{err}`")

    if BOTLOG:
        await query.client.send_message(
            BOTLOG_CHATID,
            f"Eval query {expression} was executed successfully")


# Helper code for eval.
# https://stackoverflow.com/a/57349931/974936
async def async_eval(code, **kwargs):
    # Note to self: please don't set globals here as they will be lost.
    # Don't clutter locals
    locs = {}
    # Restore globals later
    globs = globals().copy()
    # This code saves __name__ and __package into a kwarg passed to the function.
    # It is set before the users code runs to make sure relative imports work
    global_args = "_globs"
    while global_args in globs.keys():
        # Make sure there's no name collision, just keep prepending _s
        global_args = "_" + global_args
    kwargs[global_args] = {}
    for glob in ["__name__", "__package__"]:
        # Copy data to args we are sending
        kwargs[global_args][glob] = globs[glob]

    root = ast.parse(code, 'exec')
    code = root.body
    if isinstance(
            code[-1],
            ast.Expr):  # If we can use it as a lambda return (but multiline)
        code[-1] = ast.copy_location(ast.Return(
            code[-1].value), code[-1])  # Change it to a return statement
    # globals().update(**<global_args>)
    glob_copy = ast.Expr(
        ast.Call(
            func=ast.Attribute(value=ast.Call(func=ast.Name(id='globals',
                                                            ctx=ast.Load()),
                                              args=[],
                                              keywords=[]),
                               attr='update',
                               ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg=None,
                            value=ast.Name(id=global_args, ctx=ast.Load()))
            ]))
    glob_copy.lineno = 0
    glob_copy.col_offset = 0
    ast.fix_missing_locations(glob_copy)
    code.insert(0, glob_copy)
    args = []
    for a in list(map(lambda x: ast.arg(x, None), kwargs.keys())):
        a.lineno = 0
        a.col_offset = 0
        args += [a]
    fun = ast.AsyncFunctionDef(
        'tmp',
        ast.arguments(args=[],
                      vararg=None,
                      kwonlyargs=args,
                      kwarg=None,
                      defaults=[],
                      kw_defaults=[None for i in range(len(args))]), code, [],
        None)
    fun.lineno = 0
    fun.col_offset = 0
    mod = ast.Module([fun])
    comp = compile(mod, '<string>', 'exec')

    exec(comp, {}, locs)

    with temp_stdio() as out:
        result = await locs["tmp"](**kwargs)
        try:
            globals().clear()
            # Inconsistent state
        finally:
            globals().update(**globs)
        return result, out.getvalue()


# Create a temporary stdio
@contextlib.contextmanager
def temp_stdio(stdout=None, stderr=None):
    old_out = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old_out


@register(outgoing=True, pattern=r"^\.exec(?: |$)([\s\S]*)")
async def run(run_q):
    """ For .exec command, which executes the dynamically created program """
    code = run_q.pattern_match.group(1)

    if run_q.is_channel and not run_q.is_group:
        await run_q.edit("`Exec isn't permitted on channels!`")
        return

    if not code:
        await run_q.edit("``` At least a variable is required to \
execute. Use .help exec for an example.```")
        return

    if code in ("userbot.session", "config.env"):
        await run_q.edit("`That's a dangerous operation! Not Permitted!`")
        return

    if len(code.splitlines()) <= 5:
        codepre = code
    else:
        clines = code.splitlines()
        codepre = clines[0] + "\n" + clines[1] + "\n" + clines[2] + \
            "\n" + clines[3] + "..."

    command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
    process = await asyncio.create_subprocess_exec(
        executable,
        '-c',
        command.strip(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) \
        + str(stderr.decode().strip())

    if result:
        if len(result) > 4096:
            file = open("output.txt", "w+")
            file.write(result)
            file.close()
            await run_q.client.send_file(
                run_q.chat_id,
                "output.txt",
                reply_to=run_q.id,
                caption="`Output too large, sending as file`",
            )
            remove("output.txt")
            return
        await run_q.edit("**Query: **\n`"
                         f"{codepre}"
                         "`\n**Result: **\n`"
                         f"{result}"
                         "`")
    else:
        await run_q.edit("**Query: **\n`"
                         f"{codepre}"
                         "`\n**Result: **\n`No Result Returned/False`")

    if BOTLOG:
        await run_q.client.send_message(
            BOTLOG_CHATID,
            "Exec query " + codepre + " was executed successfully")


@register(outgoing=True, pattern="^\.term(?: |$)(.*)")
async def terminal_runner(term):
    """ For .term command, runs bash commands and scripts on your server. """
    curruser = getuser()
    command = term.pattern_match.group(1)
    try:
        from os import geteuid
        uid = geteuid()
    except ImportError:
        uid = "This ain't it chief!"

    if term.is_channel and not term.is_group:
        await term.edit("`Term commands aren't permitted on channels!`")
        return

    if not command:
        await term.edit("``` Give a command or use .help term for \
            an example.```")
        return

    if command in ("userbot.session", "config.env"):
        await term.edit("`That's a dangerous operation! Not Permitted!`")
        return

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) \
        + str(stderr.decode().strip())

    if len(result) > 4096:
        output = open("output.txt", "w+")
        output.write(result)
        output.close()
        await term.client.send_file(
            term.chat_id,
            "output.txt",
            reply_to=term.id,
            caption="`Output too large, sending as file`",
        )
        remove("output.txt")
        return

    if uid == 0:
        await term.edit("`" f"{curruser}:~# {command}" f"\n{result}" "`")
    else:
        await term.edit("`" f"{curruser}:~$ {command}" f"\n{result}" "`")

    if BOTLOG:
        await term.client.send_message(
            BOTLOG_CHATID,
            "Terminal Command " + command + " was executed sucessfully",
        )


CMD_HELP.update({"eval": ".eval 2 + 3\nUsage: Evalute mini-expressions."})
CMD_HELP.update(
    {"exec": ".exec print('hello')\nUsage: Execute small python scripts."})
CMD_HELP.update(
    {"term": ".term ls\nUsage: Run bash commands and scripts on your server."})
