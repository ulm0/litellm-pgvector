import os
import shutil

dims = os.environ.get("EMBEDDING__DIMENSIONS", "1536")

with open("prisma/schema.prisma.tpl") as f:
    schema = f.read()

schema = schema.replace("{{EMBEDDING_DIMENSIONS}}", dims)

with open("prisma/schema.prisma", "w") as f:
    f.write(schema)

print(f"Generated schema.prisma with vector({dims})")
