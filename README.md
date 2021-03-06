# Ideas
With so many new things I'm trying to learn, things start to get messy very easily and sometimes ideas are lost altogether.
So I made this small app that allows you to type whatever ideas you have and group them in topics so things get a bit clearer and you wouldn't have to worry about losing interesting thought anymore.


## Main page's UI

![Main page's UI](https://github.com/AChillFeeder/ideas/blob/master/screenshots/Capture.PNG)

### Add a new Idea:

![Add an idea](https://github.com/AChillFeeder/ideas/blob/master/screenshots/Capture2.PNG)

## Settings
You can change colors and enable dark mode in the settings, the profile picture change isn't functional.
Settings aren't properly done, you have to select your color and enable/disable dark theme every time you change settings, I'm sure there's a better way to do this and I'm scratching my head to find it.

![Change settings](https://github.com/AChillFeeder/ideas/blob/master/screenshots/Capture3.PNG)

### Search function:
You can filter through your ideas by typing in the search bar, only entries containing your search query will stay
By the way this is how light UI looks like! Should have avoided to show it right after dark themed pages, it looks so bright...

![Light mode UI and search function](https://github.com/AChillFeeder/ideas/blob/master/screenshots/Capture4.PNG)

## Responsive design:
The app works pretty well on phones too, here's what it looks like:

![Responsive design](https://github.com/AChillFeeder/ideas/blob/master/screenshots/Capture5.PNG)


# Stack
"Ideas" run on Python/Flask, the obvious choice would be to use databases here but I opted for a more basic Folder/TXT file approach as a temporary system until I get a database up and rolling, consider it a proof of concept or something.
The front-end side contains HTML/CSS and a bit of vanilla Javascript, no frameworks. I want to understand everything (well not EVERYTHING) there is to understand about Javascript in webdev before picking a framework so I get to know the things that happen behind the curtains, I think learning a framework too early would get me to use things I don't really understand enough.

# Future changes
- [ ] Only show the Topics, ideas should be shown separately when the user chooses a topic to delve in. 
