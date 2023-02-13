from modules.shared import cmd_opts
from modules import (
    shared,
    sd_samplers,
    upscaler,
    extensions,
    localization,
    ui_tempdir,
    ui_extra_networks,
)

if cmd_opts.server_name:
    server_name = cmd_opts.server_name
else:
    server_name = "0.0.0.0" if cmd_opts.listen else None


def setup():
    extensions.list_extensions()
    localization.list_localizations(cmd_opts.localizations_dir)
    
    
    if cmd_opts.ui_debug_mode:
        
