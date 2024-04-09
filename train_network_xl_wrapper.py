try:
    from sdxl_train_network import setup_parser, SdxlNetworkTrainer
    from library.train_util import read_config_from_file

    parser = setup_parser()
    args = parser.parse_args()
    args = read_config_from_file(args, parser)

    trainer = SdxlNetworkTrainer()
    trainer.train(args)

except:
    import sys
    import traceback
    from pygments import formatters, highlight, lexers
    from dracula import DraculaStyle

    tb = traceback.format_exc().split("\n")
    tb_text = "\n".join(tb[:-2])

    lexer = lexers.get_lexer_by_name("pytb", stripall=True)
    formatter = formatters.Terminal256Formatter(style=DraculaStyle)
    tb_colored = highlight(tb_text, lexer, formatter)

    print(f"{tb_colored}\n\033[0;31m\033[1m{tb[-2]}\n")
    sys.exit(1)
