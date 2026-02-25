import os


def ft_tqdm(lst: range) -> None:
    """Mimics tqdm progress bar using yield."""
    total = len(lst)
    for i, item in enumerate(lst, 1):
        # get terminal width to fill the bar
        cols = os.get_terminal_size().columns
        percent = i / total
        # reserve space for the text parts like "100%|>| 333/333"
        text_part = f"\r{int(percent * 100):3d}%|"
        end_part = f"| {i}/{total}"
        bar_len = cols - len(text_part) - len(end_part)
        filled = int(bar_len * percent)
        bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
        print(f"{text_part}{bar}{end_part}", end="", flush=True)
        yield item
