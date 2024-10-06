try:
    from train_network import setup_parser, NetworkTrainer
    from library.train_util import read_config_from_file

    parser = setup_parser()
    args = parser.parse_args()
    args = read_config_from_file(args, parser)

    trainer = NetworkTrainer()
    trainer.train(args)
    print("\n\033[1m✅ Done! Go download your Lora from Google Drive.\nThere will be several files, you should try the latest version (the file with the largest number next to it)")

except BaseException:
    import traceback
    import re
    from pygments import formatters, highlight, lexers
    from dracula import DraculaStyle

    tb = traceback.format_exc().split("\n")
    error_index = len(tb)
    for i, line in enumerate(tb):
      if re.match(r"^[A-Za-z-_]+Error:", line):
        error_index = i
        break
    tb_text = "\n".join(tb[:error_index])

    lexer = lexers.get_lexer_by_name("pytb", stripall=True)
    formatter = formatters.Terminal256Formatter(style=DraculaStyle)
    tb_colored = highlight(tb_text, lexer, formatter)

    print(f"\n{tb_colored}")
    if error_index < len(tb):
      tb_error = "\n".join(tb[error_index:])
      print(f"\033[0;31m\033[1m{tb_error}\n")
