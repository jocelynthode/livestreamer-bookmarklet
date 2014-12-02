livestreamer-bookmarklet
========================

These small scripts allow you to only click on a bookmarklet to launch livestreamer for twitch

For the custom protocol handler to work, I had to add the .desktop into .local/share/applications and then add in .local/share/applications/mimeapps.list  the following line : x-scheme-handler/livestreamer=livestreamer.desktop;

Don't forget to run update-desktop-database
