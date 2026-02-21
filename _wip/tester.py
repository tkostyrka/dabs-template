import sample_package.cli.main as sp

args = ["--message", "hello world"]
sp.main(args)

sp.main()


# uv run python _wip/tester.py
# uv run python _wip/tester.py --message "cli provided"
