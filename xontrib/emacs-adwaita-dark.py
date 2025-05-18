# -*- coding: utf-8 -*-
"""
    Emacs-Adwaita-Dark Theme v1.2.5

    https://github.com/zenorocha/emacs-adwaita-dark-theme

    Copyright 2025, All rights reserved

    Code licensed under the MIT license

    :author André Auzi <aauzi@free.fr>
"""

# adwaita-dark-like basic colors
# inspired by https://github.com/emacsmirror/adwaita-dark-theme
_c = {
    'background':     "#000000",
    'base-5':         "#656565",
    'black':          "#383838",
    'blue':           "#64a6f4",
    'cyan':           "#7ee5ff",
    'default':        "#00ff00",
    'green':          "#54d18c",
    'orange':         "#ffa348",
    'ptk-blue':       "#1c71d8",
    'purple':         "#dd80de",
    'red':            "#ff6c6b",
    'teal':           "#5bc8af",
    'violet':         "#dd80de",
    'white':          "#fefefe",
    'yellow':         "#f8e45c",
    
    'intense-black':  "#1c1c1c",
    'intense-blue':   "#3253ff",
    'intense-cyan':   "#3fffff",
    'intense-green':  "#00bb00",
    'intense-orange': "#ffff24",
    'intense-purple': "#ff40ff",
    'intense-red':    "#ff3636",
    'intense-white':  "#ffffff",
    'intense-yellow': "#fff053",
}

# syntactic hilight elements
# font-lock equivalence
# deviations:
# - fg is white, bg is black
# - do not use bold for type and regexp grouping.
# - use violet/purple for comments instead of base-5 (which seems too dark to me).
# - added generic elements are (mostly-)green (red for deleted though). 
_s = {
    'default':     _c['white'],
    'bold':        f"bold {_c['default']}",
    'italic':      f"italic {_c['default']}",
    'italic-bold': f"italic bold {_c['default']}",
    'strong':      _c['intense-green'],
    'heading':     f"bold {_c['default']}",
    'sub-heading': _c['base-5'],
    'deleted':     _c['red'],
    'inserted':    _c['green'],
    'error':       _c['intense-red'],
    'warning':     _c['intense-yellow'],
    'comment':     _c['violet'],
    'constant':    _c['blue'],   # Ex. None, True, False
    'entity':      _c['blue'],   # Ex. print()
    'keyword':     f"bold {_c['orange']}", # Ex. if
    'decorator':   _c['green'],
    'type':        _c['teal'],   # not f"bold {_c['teal']}",
    'string':      _c['teal'],
    'variable':    _c['white'],
}

# gtk-like color hilightings
_p = {
    'black': f"bg:{_c['ptk-blue']} {_c['intense-black']}",
    'white':f"bg:{_c['ptk-blue']} {_c['intense-white']}",
}

# adwaita-dark-like xonsh colors
_adwaita_dark_colors = {
    'Color.BLACK':          _c['black'],
    'Color.BLUE':           _c['blue'],
    'Color.CYAN':           _c['cyan'],
    'Color.DEFAULT':        _c['default'],
    'Color.GREEN':          _c['green'],
    'Color.INTENSE_BLACK':  _c['intense-black'],
    'Color.INTENSE_BLUE':   _c['intense-blue'],
    'Color.INTENSE_CYAN':   _c['intense-cyan'],
    'Color.INTENSE_GREEN':  _c['intense-green'],
    'Color.INTENSE_PURPLE': _c['intense-purple'],
    'Color.INTENSE_RED':    _c['intense-red'],
    'Color.INTENSE_WHITE':  _c['intense-white'],
    'Color.INTENSE_YELLOW': _c['intense-yellow'],
    'Color.PURPLE':         _c['purple'],
    'Color.RED':            _c['red'],
    'Color.WHITE':          _c['white'],
    'Color.YELLOW':         _c['yellow'],
}

# pygments 'Tokens' (see https://pygments.org/docs/tokens/), version: 2.19.1
_emacs_tokens = {
    'Token.Keyword':                        _s['keyword'],     # any other than the subtypes
    'Token.Keyword.Constant':               _s['constant'],    # constants (e.g. None, True, False)
    'Token.Keyword.Declaration':            _s['keyword'],     # variable declaration (e.g. var in JavaScript)
    'Token.Keyword.Namespace':              _s['keyword'],     # namespace declarations (e.g. import).
    'Token.Keyword.Pseudo':                 _s['entity'],      # not really keywords (e.g. None in old Python versions).
    'Token.Keyword.Reserved':               _s['keyword'],     # reserved keywords (e.g. TBD)
    'Token.Keyword.Type':                   _s['type'],        # builtin types that can’t be used as identifiers (e.g. str, int TBC)
    
    'Token.Name':                           _s['variable'],    # any name (variable, function, classes).
    'Token.Name.Attribute':                 _s['variable'],    # attributes (e.g. in HTML tags).
    'Token.Name.Builtin':                   _s['entity'],      # builtins and names that are available in the global namespace.
    'Token.Name.Builtin.Pseudo':            _s['keyword'],     # Builtin names that are implicit (e.g. self).
    'Token.Name.Class':                     _s['type'],        # meant for class declarations
    'Token.Name.Constant':                  _s['constant'],    # special entities. (e.g. &nbsp; in HTML)
    'Token.Name.Decorator':                 _s['decorator'],
    'Token.Name.Entity':                    _s['entity'],
    'Token.Name.Exception':                 _s['variable'],
    'Token.Name.Function':                  _s['entity'],
    'Token.Name.Function.Magic':            _s['entity'],      # function names that have an implicit use in a language (e.g. __init__)
    'Token.Name.Label':                     _s['bold'],
    'Token.Name.Namespace':                 _s['variable'],    # namespaces. (e.g. import paths)         
    'Token.Name.Other':                     _s['keyword'],     # normally not used
    'Token.Name.Property':                  _s['variable'],             
    'Token.Name.Tag':                       _s['constant'],
    'Token.Name.Variable':                  _s['variable'],
    'Token.Name.Variable.Class':            _s['variable'],             
    'Token.Name.Variable.Global':           _s['variable'],             
    'Token.Name.Variable.Instance':         _s['variable'],             
    'Token.Name.Variable.Magic':            _s['entity'],      # special variable names that have an implicit use (e.g. __doc__ )           
    
    'Token.Literal':                        _s['default'],
    'Token.Literal.Date':                   _s['constant'],
    'Token.Literal.String':                 _s['string'],
    'Token.Literal.String.Affix':           _s['default'],
    'Token.Literal.String.Char':            _s['string'],
    'Token.Literal.String.Doc':             _s['comment'],
    'Token.Literal.String.Single':          _s['string'],
    'Token.Literal.String.Double':          _s['string'],
    'Token.Literal.String.Heredoc':         _s['comment'],
    'Token.Literal.String.Escape':          _s['string'],
    'Token.Literal.String.Backtick':        _s['string'],
    'Token.Literal.String.Interpol':        _s['string'],
    'Token.Literal.String.Other':           _s['string'],
    'Token.Literal.String.Regex':           _s['string'],
    'Token.Literal.String.Symbol':          _s['entity'],

    'Token.String':                         _s['string'],
    'Token.Number':                         _s['default'],
    'Token.Number.Bin':                     _s['default'],
    'Token.Number.Float':                   _s['default'],
    'Token.Number.Hex':                     _s['default'],
    'Token.Number.Integer':                 _s['default'],
    'Token.Number.Integer.Long':            _s['default'],
    'Token.Number.Oct':                     _s['default'],
    
    'Token.Operator':                       _s['default'],
    'Token.Operator.Word':                  _s['keyword'],
    
    'Token.Other':                          _s['default'],
    'Token.Other.Constant':                 _s['constant'],
    
    'Token.Punctuation':                    _s['default'],
    'Token.Punctuation.Marker':             _s['default'],
    'Token.Punctuation.Definition.Comment': _s['comment'],

    'Token.Comment':                        _s['comment'],
    'Token.Comment.Hashbang':               _s['comment'],
    'Token.Comment.Multiline':              _s['comment'],
    'Token.Comment.Preproc':                _s['comment'],
    'Token.Comment.PreprocFile':            _s['comment'],
    'Token.Comment.Single':                 _s['comment'],
    'Token.Comment.Special':                _s['comment'],
    
    'Token.Generic':                        _s['default'],
    'Token.Generic.Deleted':                _s['deleted'],
    'Token.Generic.Emph':                   _s['italic'],
    'Token.Generic.EmphStrong':             _s['italic-bold'],
    'Token.Generic.Error':                  _s['error'],
    'Token.Generic.Heading':                _s['heading'],
    'Token.Generic.Inserted':               _s['inserted'],
    'Token.Generic.Prompt':                 _s['default'],
    'Token.Generic.Strong':                 _s['strong'],
    'Token.Generic.Subheading':             _s['sub-heading'],
    'Token.Generic.Output':                 _s['default'],
    'Token.Generic.Traceback':              _s['default'],
    
    'Token.Whitespace':                     _s['default'],    
    'Token.Error':                          _s['error'],
    'Token.Warning':                        _s['warning'], # does not exist but you never know
}

del _s

# gtk-like colors for the prompt_toolkit completion suggestions/interactions
_ptk_tokens = {
    'Token.PTK.Aborting':                          _p['black'],
    'Token.PTK.AutoSuggestion':                    _p['black'],
    'Token.PTK.CompletionMenu':                    _p['white'],
    'Token.PTK.CompletionMenu.Completion':         _p['white'], 
    'Token.PTK.CompletionMenu.Completion.Current': _p['white'], 
    'Token.PTK.Scrollbar.Arrow':                   _p['white'],
    'Token.PTK.Scrollbar.Background':              _p['white'],
    'Token.PTK.Scrollbar.Button':                  _p['white'],
}

del _p

_emacs_adwaita_dark = dict(_adwaita_dark_colors)
_emacs_adwaita_dark.update(_emacs_tokens)
_emacs_adwaita_dark.update(_ptk_tokens)

del _adwaita_dark_colors
del _emacs_tokens
del _ptk_tokens

from xonsh.tools import register_custom_style

register_custom_style("emacs-adwaita-dark",
                      _emacs_adwaita_dark,
                      background_color=_c['background'],
                      base="default")

del _c
del _emacs_adwaita_dark

