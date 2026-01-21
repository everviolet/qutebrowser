from .palette import palette

def setup(c, variant, samecolorrows = False):
    p = palette[variant]

    # completion {{{
    ## Background color of the completion widget category headers.
    c.colors.completion.category.bg = p["base"]
    ## Bottom border color of the completion widget category headers.
    c.colors.completion.category.border.bottom = p["mantle"]
    ## Top border color of the completion widget category headers.
    c.colors.completion.category.border.top = p["overlay2"]
    ## Foreground color of completion widget category headers.
    c.colors.completion.category.fg = p["green"]
    ## Background color of the completion widget for even and odd rows.
    if samecolorrows:
        c.colors.completion.even.bg = p["mantle"]
        c.colors.completion.odd.bg = c.colors.completion.even.bg
    else:
        c.colors.completion.even.bg = p["mantle"]
        c.colors.completion.odd.bg = p["crust"]
    ## Text color of the completion widget.
    c.colors.completion.fg = p["subtext0"]

    ## Background color of the selected completion item.
    c.colors.completion.item.selected.bg = p["surface2"]
    ## Bottom border color of the selected completion item.
    c.colors.completion.item.selected.border.bottom = p["surface2"]
    ## Top border color of the completion widget category headers.
    c.colors.completion.item.selected.border.top = p["surface2"]
    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.fg = p["text"]
    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.match.fg = p["cherry"]
    ## Foreground color of the matched text in the completion.
    c.colors.completion.match.fg = p["text"]

    ## Color of the scrollbar in completion view
    c.colors.completion.scrollbar.bg = p["crust"]
    ## Color of the scrollbar handle in completion view.
    c.colors.completion.scrollbar.fg = p["surface2"]
    # }}}

    # downloads {{{
    c.colors.downloads.bar.bg = p["base"]
    c.colors.downloads.error.bg = p["base"]
    c.colors.downloads.start.bg = p["base"]
    c.colors.downloads.stop.bg = p["base"]

    c.colors.downloads.error.fg = p["red"]
    c.colors.downloads.start.fg = p["blue"]
    c.colors.downloads.stop.fg = p["green"]
    c.colors.downloads.system.fg = "none"
    c.colors.downloads.system.bg = "none"
    # }}}

    # hints {{{
    ## Background color for hints. Note that you can use a `rgba(...)` value
    ## for transparency.
    c.colors.hints.bg = p["orange"]

    ## Font color for hints.
    c.colors.hints.fg = p["mantle"]

    ## Hints
    c.hints.border = "1px solid " + p["mantle"]

    ## Font color for the matched part of hints.
    c.colors.hints.match.fg = p["subtext1"]
    # }}}

    # keyhints {{{
    ## Background color of the keyhint widget.
    c.colors.keyhint.bg = p["mantle"]

    ## Text color for the keyhint widget.
    c.colors.keyhint.fg = p["text"]

    ## Highlight color for keys to complete the current keychain.
    c.colors.keyhint.suffix.fg = p["subtext1"]
    # }}}

    # messages {{{
    ## Background color of an error message.
    c.colors.messages.error.bg = p["overlay0"]
    ## Background color of an info message.
    c.colors.messages.info.bg = p["overlay0"]
    ## Background color of a warning message.
    c.colors.messages.warning.bg = p["overlay0"]

    ## Border color of an error message.
    c.colors.messages.error.border = p["mantle"]
    ## Border color of an info message.
    c.colors.messages.info.border = p["mantle"]
    ## Border color of a warning message.
    c.colors.messages.warning.border = p["mantle"]

    ## Foreground color of an error message.
    c.colors.messages.error.fg = p["red"]
    ## Foreground color an info message.
    c.colors.messages.info.fg = p["text"]
    ## Foreground color a warning message.
    c.colors.messages.warning.fg = p["orange"]
    # }}}

    # prompts {{{
    ## Background color for prompts.
    c.colors.prompts.bg = p["mantle"]

    # ## Border used around UI elements in prompts.
    c.colors.prompts.border = "1px solid " + p["overlay0"]

    ## Foreground color for prompts.
    c.colors.prompts.fg = p["text"]

    ## Background color for the selected item in filename prompts.
    c.colors.prompts.selected.bg = p["surface2"]

    ## Background color for the selected item in filename prompts.
    c.colors.prompts.selected.fg = p["cherry"]
    # }}}

    # statusbar {{{
    ## Background color of the statusbar.
    c.colors.statusbar.normal.bg = p["base"]
    ## Background color of the statusbar in insert mode.
    c.colors.statusbar.insert.bg = p["crust"]
    ## Background color of the statusbar in command mode.
    c.colors.statusbar.command.bg = p["base"]
    ## Background color of the statusbar in caret mode.
    c.colors.statusbar.caret.bg = p["base"]
    ## Background color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.bg = p["base"]

    ## Background color of the progress bar.
    c.colors.statusbar.progress.bg = p["base"]
    ## Background color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.bg = p["base"]

    ## Foreground color of the statusbar.
    c.colors.statusbar.normal.fg = p["text"]
    ## Foreground color of the statusbar in insert mode.
    c.colors.statusbar.insert.fg = p["cherry"]
    ## Foreground color of the statusbar in command mode.
    c.colors.statusbar.command.fg = p["text"]
    ## Foreground color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.fg = p["orange"]
    ## Foreground color of the statusbar in caret mode.
    c.colors.statusbar.caret.fg = p["orange"]
    ## Foreground color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.fg = p["orange"]

    ## Foreground color of the URL in the statusbar on error.
    c.colors.statusbar.url.error.fg = p["red"]

    ## Default foreground color of the URL in the statusbar.
    c.colors.statusbar.url.fg = p["text"]

    ## Foreground color of the URL in the statusbar for hovered links.
    c.colors.statusbar.url.hover.fg = p["skye"]

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.http.fg = p["aqua"]

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.https.fg = p["green"]

    ## Foreground color of the URL in the statusbar when there's a warning.
    c.colors.statusbar.url.warn.fg = p["yellow"]

    ## PRIVATE MODE COLORS
    ## Background color of the statusbar in private browsing mode.
    c.colors.statusbar.private.bg = p["mantle"]
    ## Foreground color of the statusbar in private browsing mode.
    c.colors.statusbar.private.fg = p["subtext1"]
    ## Background color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.bg = p["base"]
    ## Foreground color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.fg = p["subtext1"]

    # }}}

    # tabs {{{
    ## Background color of the tab bar.
    c.colors.tabs.bar.bg = p["crust"]
    ## Background color of unselected even tabs.
    c.colors.tabs.even.bg = p["surface2"]
    ## Background color of unselected odd tabs.
    c.colors.tabs.odd.bg = p["surface1"]

    ## Foreground color of unselected even tabs.
    c.colors.tabs.even.fg = p["overlay2"]
    ## Foreground color of unselected odd tabs.
    c.colors.tabs.odd.fg = p["overlay2"]

    ## Color for the tab indicator on errors.
    c.colors.tabs.indicator.error = p["red"]
    ## Color gradient interpolation system for the tab indicator.
    ## Valid values:
    ##	 - rgb: Interpolate in the RGB color system.
    ##	 - hsv: Interpolate in the HSV color system.
    ##	 - hsl: Interpolate in the HSL color system.
    ##	 - none: Don't show a gradient.
    c.colors.tabs.indicator.system = "none"

    # ## Background color of selected even tabs.
    c.colors.tabs.selected.even.bg = p["base"]
    # ## Background color of selected odd tabs.
    c.colors.tabs.selected.odd.bg = p["base"]

    # ## Foreground color of selected even tabs.
    c.colors.tabs.selected.even.fg = p["text"]
    # ## Foreground color of selected odd tabs.
    c.colors.tabs.selected.odd.fg = p["text"]
    # }}}

    # context menus {{{
    c.colors.contextmenu.menu.bg = p["base"]
    c.colors.contextmenu.menu.fg = p["text"]

    c.colors.contextmenu.disabled.bg = p["mantle"]
    c.colors.contextmenu.disabled.fg = p["overlay0"]

    c.colors.contextmenu.selected.bg = p["overlay0"]
    c.colors.contextmenu.selected.fg = p["cherry"]
    # }}}

# vim:fileencoding=utf-8:foldmethod=marker
