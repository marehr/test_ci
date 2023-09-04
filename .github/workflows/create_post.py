from string import Template

post_template = Template("""
---
layout: elternbrief
title: "${title}"
date: "${date}"
category: elternbrief
---

${post_body}

""")

def main():
    import os

    post = {
        id: os.environ['ISSUE_ID']
        title: os.environ['ISSUE_TITLE']
        body: os.environ['ISSUE_BODY']
        created_at: os.environ['ISSUE_CREATED_AT']
        updated_at: os.environ['ISSUE_UPDATED_AT']
    }

    print (f"post_id: {post.id}")
    print (f"post_title: {post.title}")
    print (f"post_body: {post.body}")
    print (f"post_created_at: {post.created_at}")
    print (f"post_updated_at: {post.updated_at}")

    print (post_template.substitute(**post))

if __name__ == "__main__":
    main()