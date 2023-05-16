# window.py
#
# Copyright 2023 Sebastian Kutter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/de/skutter/GeminiBrowser/window.ui')
class GeminiBrowserWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'GeminiBrowserWindow'

    label = Gtk.Template.Child()
    my_button = Gtk.Template.Child()
    my_button_click_counter = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback("on_my_button_clicked")
    def on_my_button_clicked(self, button):
        self.my_button_click_counter += 1
        self.label.set_text(f"clicked {self.my_button_click_counter} times")
