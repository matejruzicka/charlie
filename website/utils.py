import enum


class FileTypes(enum.Enum):
    pdf = "application/pdf"
    doc = "application/msword"
    docx = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    jpg = "image/jpeg"
    jpeg = "image/jpeg"
    png = "image/png"


if __name__ == "__main__":
    print(FileTypes["pdf"].value)
