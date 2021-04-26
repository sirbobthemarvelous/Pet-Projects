import random
import PySimpleGUI as sg

#take canon stuff https://docs.google.com/document/d/17sQvioYmtanVqlapHa2TYacd9FSg5KiKilsbkmA-4z8/edit
#then u can pull new stuff https://grammar.yourdictionary.com/word-lists/nature-words-vocabulary-list.html
#maybe add skyclan or warrior clan stuff
nature_stuff = ['Fire','Gray','Heart','Stripe','Lion','Blue','Fur','White','Storm','Red','Tail',
'Ash','Barley','Black','Foot','Bright','Flower','Brindle','Face','Broken','Claw','Crooked','Jaw','Dapple',
'Dark','Dawn','Cloud','Dust','Elder','Frost','Pelt','Golden','Half','Long','Mouse','Oak','One','Eye','Patch',
'Ragged','Raven','Rose','Running','Nose','Wind','Sand','Small','Ear','Speckle','Spotted',
'Leaf','Swamp','Tiger','Willow','Yellow','Fang','Bark','Bracken','Cinder','Dead','Leopard','Mistle','Morning',
'Night','Whisker','Silver','Stream','Swift','Tall','Tulip','Wet','Lynx','Quail',
'Stork','Nut','Brown','Crow','Pool','Green','Misty','Mud','Stone','Stumpy','Swan',
'Thorn','Torn','Boulder','Bramble','Fern','Gorse','Little','Moss','Brook','Snow',
'Throat','Feather','Lost','Loud','Belly','Shade','Tawny','Cricket','Bone','Jagged','Tooth',
'Hawk','Holly','Larch','Rain','Shrew','Sorrel','Soot','Wing','Russet','Cedar','Crag','Rock','Talon','Teller',
'Scree','Water','Sky','Eagle','Mist','Sun','Bird','Marsh','Oat','Robin','Smoke','Splash','Poppy',
'Thistle','Tumble','Shadow','Daisy','Rush','Spider','Leg','Swallow','Squirrel','Flight','Heavy','Step',
'Birch','Ivy','Owl','Reed','Vole','Weasel','Berry','Rowan','Fall','Breeze','Buzzard','Heather','Jay','Blaze','Mole',
'Fleet','Petal','Thrush','Cherry','Clover','Down','Echo','Song','Fawn','Fox','Hare','Hill','Ice','Kestrel','Lark',
'Lily','Milk','Prickle','Rose','Snake','Sloe','Watcher','Tangle','Twig','Fallen','Leaves','Hazel','Blossom','Adder',
'Dew','Spots','Spot','Honey','Kink','Nettle','Pine','Shine','Spirit','Brave','Moon','Lightning','Rising','Shy','Falcon',
'Dove','River','Falcon','Fish','Furl','Acorn','Aspen','Badger','Bee','Blizzard','Drift','Eel','Hay','Jump','Lake','Log',
'Maple','Meadow','Minnow','Moth','Mottle','Mask','Odd','Pebble','Ripple','Rubble','Rye','Sheep','Slate','Small','Sunny',
'Trout','Vine','Wild','Wolf','Fuzzy','Mumble','Sweet','Weed','Chestnut','Flame','Leap','Otter','Wood','Toad','Spring',
'Shred','Rat','Scar','Fennel','Fly','Snapper','Pear','Pike','Sedge','Rabbit','Bounce','Dodge','Lichen','Tiny','Wasp',
'Apple','Olive','Pale','Sparrow','Chase','Strong','Dusk','Stem','Shell','Shimmer','Soft','Timber','Vixen','Ant',
'Ferret','Furze','Hollow','Maggot','Starling','Mint','Yarrow','Plum','Primrose','Amber','Arch','Deer','Finch','Flint',
'Frog','Hope','Wish','Bear','Newt','Ember','Hatch','Seed','Snail','Stoat','Clear','Peak','Roar','Quiet','Sharp','Hail',
'Doe','Flail','Hikory','Bumble','Dart','Turtle','Branch','Fircone','Tansy','Bluebell','Dance','Melt','Midge','Pink','Juniper',
'Chive','Snout','Hound','Stag','Rook','Muzzle','Needle','Alder','Dandelion','Perch','Spark','Sneeze','Cypress','Silt',
'Wasp','Wave','Curly','Freckle','Parsley','Snip','Sage','Crystal','Briar','Sleek','Shiver','Burrow','Marigold','Spire',
'Sight','Pod','Tree','Violet','Haven','Haze','Bristle','Lizard','Whorl',
'Root','Fringe','Flicker','Tempest','Hop','Scratch','Root','Bay','Myrtle']
def name_generate():
    prefix = random.randint(0,int(len(nature_stuff)-1))
    suffix = random.randint(0,int(len(nature_stuff)-1))
    while prefix == suffix:
        suffix = random.randint(int(0,len(nature_stuff)-1))
    return nature_stuff[prefix]+nature_stuff[suffix]
#i guess I could add Descriptions in there too
#but I'm more interested in NARRATIVE role generator
#then...Narrative role that interacts with Others, batch generator

layout = [[sg.Text("Hello from PySimpleGUI")], 
        [sg.Button("Generate")],
        [sg.Text("Blank Space")]]

# Create the window
window = sg.Window("Warrior name Generator v0.1", layout)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Generate":
        sg.Popup('The New Name',
         name_generate())
    
    if event == sg.WIN_CLOSED:
        break

window.close()