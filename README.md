### Eye of Gnome xmp rating plugin

This is just what I need to sort my photos but it could be a good start for somebody that wants to create a proper xmp rating plugin

At the time it only allows modifying the xmp rating via menu or shortcuts

It does not:

* refresh the rating on the eog properties window (you have to manually reload the image)
* show the current rating as a checkbox on the menu
* have toolbar buttons

It requires pyexiv2 and on latest Ubuntu Gnome you have to put it in ` $HOME/.local/share` because `XDG_DATA_HOME` is empty and defaults to that
