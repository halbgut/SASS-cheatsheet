# SASS Cheatsheet
## Syntax
### Declarations
```sass
	border: 1px solid tomato
```

### Imports
```sass
	@import components/code
```
### Mixins
#### Defining Mixins
```sass
	=bounce ($param1, $param2)
		<Your mixin here>
```
#### Calling Mixins
```sass
	+bounce (yolo, swag)
```
### Defining Maps and Lists
```sass
	$var-map: ( fresh: killazz, hashtag: mofo )
	$var-list: yolo, zolo, molo, tolo
```
**Invalid:**
```sass
	$var-map: (
		guess: 23,
		answer: 42
	)
```
Note: Same goes for lists
This is awful but:
*Planned - /issues/216 - 13 Aug 14*
*/u/myabc made a PQ; rejected by /u/nex3 (/pull/1504)*

### Shorthand properties #UNDOCUMENTED
```sass
	font:
		family: "Comic Sans", Arial
		size: 2em
```
## Mixins (SASS & SCSS)
### List (all work with maps too)
```sass
	length($var-list)
	nth($var-list, 3)
```

```sass
	$var-map: join($var-list, $another-list)
```
Turns maps to a two dimentional list.
```sass
	index($var-list, molo)
	$var-map: append($var-list, kolo)
	$zipped-list: zip($list1, $list2)
```
### Maps
```sass
	$var-map: map-get($var-map, killaz)
	$var-map: map-merge($var-map, (AAaaa: Oooo))
	$var-map: map-remove($var-map, fresh)
```
```sass
	map-keys($var-map)
```
Returns a list of keys
```sass
	map-values($var-map)
```
Returns a list of values
```sass
	map-has-key($var-map, hashtag)
```
### Debugging
```sass
	inspect()
```

### Strings
```sass
	quote($string)
	unquote($string)
	str-length($string)
	str-index($string)
	str-slice($string, 0, 4)
	str-slice($string, 4)
	to-upper-case($string)
	to-lower-case($string)
```

### Meta Stuff
```sass
	feature-exists($feature)
```
This is only for plugins
```sass
	[[global-]variable|function|mixin]-exists($thing)
	type-of($var-list)
	unit(1rem)
	unitless(3)
```
```sass
	comparable(1px, 1px)
```
Checks if two values have the same unit
```sass
	call($function-name, $arg1, $arg2)
```
This opens up a whole (new) world
```sass
	unique-id()
```
Returns something like "uanlk2zlx"

### Colors, Numbers
I'm bad with colors and numbers soo I'm leaving this out.

### Se