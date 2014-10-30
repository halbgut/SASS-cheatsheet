# SASS Cheatsheet
## Syntax
### Declarations
	border: 1px solid tomato

### Imports
	@import components/code

### Mixins
#### Defining Mixins
	=bounce ($param1, $param2)
		<Your mixin here>

#### Calling Mixins
	+bounce (yolo, swag)

### Defining Maps and Lists
	$var-map: ( fresh: killazz, hashtag: mofo )
	$var-list: yolo, zolo, molo, tolo
**Invalid:**
	$var-map: (
		guess: 23,
		answer: 42
	)
Note: Same goes for lists
This is awful but:
*Planned - /issues/216 - 13 Aug 14*

### Shorthand properties #UNDOCUMENTED
	font:
		family: "Comic Sans", Arial
		size: 2em

### Variable defaults
	$answer-to-question || No!

## Mixins (SASS & SCSS)
### List (all work with maps too)
	length($var-list)
	nth($var-list, 3)

	$var-map: join($var-list, $another-list)
Turns maps to a two dimentional list.

	index($var-list, molo)
	$var-map: append($var-list, kolo)
	$zipped-list: zip($list1, $list2)

### Maps
	$var-map: map-get($var-map, killaz)
	$var-map: map-merge($var-map, (AAaaa: Oooo))
	$var-map: map-remove($var-map, fresh)

	map-keys($var-map)
Returns a list of keys

	map-values($var-map)
Returns a list of values

	map-has-key($var-map, hashtag)

### Debugging
	inspect()

### Strings
	quote($string)
	unquote($string)
	str-length($string)
	str-index($string)
	str-slice($string, 0, 4)
	str-slice($string, 4)
	to-upper-case($string)
	to-lower-case($string)

### Meta Stuff
	feature-exists($feature)
This is only for plugins

	[[global-]variable|function|mixin]-exists($thing)
	type-of($var-list)
	unit(1rem)
	unitless(3)

	comparable(1px, 1px)
Checks if two values have the same unit

	call($function-name, $arg1, $arg2)
This opens up a whole (new) world

	unique-id()
Returns something like "uanlk2zlx"

### Colors, Numbers
I'm bad with colors and numbers soo I'm leaving this out.

