# Copyright (C) 2014 - Michael Demetriou
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.


from gi.repository import GObject, Eog, Gtk
import pyexiv2

ui_str = """
	<ui>
	  <menubar name="MainMenu">
	    <menu name="ToolsMenu" action="Tools">
	      <separator/>
	        <menuitem name="Set Rating To 0" action="Rating0" />
	      	<menuitem name="Set Rating To 1" action="Rating1" /> 
	        <menuitem name="Set Rating To 2" action="Rating2" /> 
		<menuitem name="Set Rating To 3" action="Rating3" /> 
		<menuitem name="Set Rating To 4" action="Rating4" /> 
		<menuitem name="Set Rating To 5" action="Rating5" /> 
	      <separator/>
	    </menu>
	  </menubar>
	</ui>
	"""

class HelloWorldPlugin(GObject.Object, Eog.WindowActivatable):
        # Override EogWindowActivatable's window property
        # This is the EogWindow this plugin instance has been activated for
        window = GObject.property(type=Eog.Window)
	data = dict()

        def __init__(self):
                GObject.Object.__init__(self)

        def do_activate(self):
		data = self.data
		ui_manager = self.window.get_ui_manager()
		data['group'] = Gtk.ActionGroup('Ratings')
		data['group'].add_actions([('Rating0', None, 'Rating _0', "<Primary>A", None, self.setRating)], 0)
		data['group'].add_actions([('Rating1', None, 'Rating _1', "<Primary>1", None, self.setRating)], 1)
		data['group'].add_actions([('Rating2', None, 'Rating _2', "<Primary>2", None, self.setRating)], 2)
		data['group'].add_actions([('Rating3', None, 'Rating _3', "<Primary>3", None, self.setRating)], 3)
		data['group'].add_actions([('Rating4', None, 'Rating _4', "<Primary>4", None, self.setRating)], 4)
		data['group'].add_actions([('Rating5', None, 'Rating _5', "<Primary>5", None, self.setRating)], 5)
		ui_manager.insert_action_group(data['group'], 0)
		data['ui_id'] = ui_manager.add_ui_from_string(ui_str)
		my_accelerators = Gtk.AccelGroup()
		self.window.add_accel_group(ui_manager.get_accel_group())

                print 'xmp rating enabled'

        def do_deactivate(self):
		data = self.data
		ui_manager = self.window.get_ui_manager()
		ui_manager.remove_ui(data['ui_id'])
		ui_manager.remove_action_group(data['group'])
		ui_manager.ensure_update()
                print 'xmp rating disabled'
	
	def setRating(self, event, value):
		print value
		img = self.window.get_image()
		if(img):
			f = img.get_file()
			print f.get_path()
			metadata = pyexiv2.ImageMetadata(f.get_path())
			metadata.read()
			print metadata.xmp_keys
			metadata['Xmp.xmp.Rating'] = value
			metadata.write()
			
			

	
