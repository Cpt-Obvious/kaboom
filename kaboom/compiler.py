import os.path
import subprocess


def compile_cli(cmd, args, filename):
    try:
        output = subprocess.check_output([cmd] + args + [filename], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise CompilationException(e.output)

    return output.strip()


def compile(filename):
    extension = os.path.splitext(filename)[1]
    if extension in ['.lll']:
        return compile_cli("lllc", [], filename)
    elif extension in ['.mu']:
        return compile_cli("mutan", [], filename)
    elif extension in ['.se']:
        return compile_cli("serpent", ["compile"], filename)
    else:
        raise CompilationException("Unknown file extension")


class CompilationException(Exception):
    pass
