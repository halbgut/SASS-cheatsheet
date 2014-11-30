# SASS Cheatsheet
## Syntax
### Declarations
```stylus
	border: 1px solid tomato
```

### Imports
```stylus
	@import components/code
```
### Mixins
#### Defining Mixins
```stylus
	=bounce ($param1, $param2)
		<Your mixin here>
```
#### Calling Mixins
```stylus
	+bounce (yolo, swag)
```
### Defining Maps and Lists
```stylus
	$var_map: ( fresh: killazz, hashtag: mofo )
	$var_list: yolo, zolo, molo, tolo
```
**Invalid:**
```stylus
	$var_map: (
		guess: 23,
		answer: 42
	)
```
Note: Same goes for lists
This is awful but:
*Planned - /issues/216 - 13 Aug 14*
*/u/myabc made a PQ; rejected by /u/nex3 (/pull/1504)*

### Shorthand properties #UNDOCUMENTED
```stylus
	font:
		family: "Comic Sans", Arial
		size: 2em
```
## Mixins (SASS & SCSS)
### List (all work with maps too)
```stylus
	length($var_list)
	nth($var_list, 3)
```

```stylus
	$var_map: join($var_list, $another_list)
```
Turns maps to a two dimentional list.
```stylus
	index($var_list, molo)
	$var_map: append($var_list, kolo)
	$zipped_list: zip($list1, $list2)
```
### Maps
```stylus
	$var_map: map-get($var_map, killaz)
	$var_map: map-merge($var_map, (AAaaa: Oooo))
	$var_map: map-remove($var_map, fresh)
```
```stylus
	map-keys($var_map)
```
Returns a list of keys
```stylus
	map-values($var_map)
```
Returns a list of values
```stylus
	map-has-key($var_map, hashtag)
```
### Debugging
```stylus
	inspect()
```

### Strings
```stylus
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
```stylus
	feature-exists($feature)
```
This is only for plugins
```stylus
	[[global-]variable|function|mixin]-exists($thing)
	type-of($var_list)
	unit(1rem)
	unitless(3)
```
```stylus
	comparable(1px, 1px)
```
Checks if two values have the same unit
```stylus
	call($function_name, $arg1, $arg2)
```
This opens up a whole (new) world
```stylus
	unique-id()
```
Returns something like "uanlk2zlx"

### Colors, Numbers
I'm bad with colors and numbers soo I'm leaving this out.

### Se