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

	join($var-list, $another-list)
Turns maps to a two dimentional list.

	index($var-list, molo)

### Maps
	map-get($var-map, killaz)
	map-merge($var-map, (AAaaa: Oooo))
	map-remove($var-map, fresh)

	map-keys($var-map)
Returns a list of keys

	map-values($var-map)
Returns a list of values

	map-has-key($var-map, hashtag)

### Debugging
	inspect()

