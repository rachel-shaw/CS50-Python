"""
GOAL:
- implement a program rthat prompts the user for the name of a file
- then outputs that file's media type (case insensitive)
- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip
- otherwise, output application/octet/stream
"""

def main():
    filename = input("File name: ").strip().lower()

    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".jpg") or filename.endswith("jpeg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet/stream")


main()


