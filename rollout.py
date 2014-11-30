import os, time, sys, datetime
mdFile = 'sass-cheatsheet.md'
toThisJs = 'js/sass-cheatsheet.js'
jsFormat = 'var sassCheatsheet = \'%s\';'

def sanitizeJs (js):
	jsSpecialChars = {'\'': '\\\'', '\n': '\\n'}
	for key in jsSpecialChars:
		js = js.replace(key, jsSpecialChars[key])
	return js

def main ():
	repeater = True
	while repeater:
		writeJs()
		sys.stdout.write('Writing JS file - ' + str(datetime.datetime.now().time()) + '...')
		sys.stdout.flush()
		sys.stdout.write("\b"*36)
		time.sleep(4)

def writeJs ():
	mdFileRes = open(mdFile, 'r')
	rawMd = mdFileRes.read()
	mdFileRes.close()
	rawMd = sanitizeJs(rawMd)
	insertThisJs = jsFormat % rawMd
	jsFile = open(toThisJs, 'w')
	jsFile.write(insertThisJs)
	jsFile.close()

if __name__ == '__main__':
	main()