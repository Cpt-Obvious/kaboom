import subprocess


def compile_cli(cmd, args, filename):
    try:
        output = subprocess.check_output([cmd] + args + [filename], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise CompilationException(e.output)

    return output.strip().decode('hex')


def compile_lll(filename):
    return compile_cli("lllc", [], filename)


class CompilationException(Exception):
    pass
