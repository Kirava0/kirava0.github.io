"""
script that creates the blogData.js file
"""
import os

POST_DIRECTORY = "posts"

paths = []

for file in os.listdir(POST_DIRECTORY):
	if file.endswith(".txt"):
		paths.append(os.path.join(POST_DIRECTORY, file))

blogdata = "const blogData = [\n"

for path in paths:
	with open(path, "r") as f:
		blogdata += "`" + f.read() + "`,\n"

blogdata += "\n];"

with open("blogData.js", "w") as f:
	f.write(blogdata)

print("finished writing blogData.js")