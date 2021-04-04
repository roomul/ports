# i3pystatus
# bar() {
#   status_command    python <path to>/panel.py
#   position          top
#   workspace_buttons yes
#}

from i3pystatus import Status

status = Status()

status.register("clock",
    format="%a %-d %b %X",)

status.register("disk",
    path="/",
    format="{used}/{total}G",)

status.register("mem",
    format="{used_mem}/{total_mem}",)

status.run()
