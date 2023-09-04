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

    def parse_date(date_str):
        import dateutil.parser
        datetime = dateutil.parser.isoparse(date_str)
        return datetime

    post = {
        'id': os.environ['ISSUE_ID'], 
        'title': os.environ['ISSUE_TITLE'], 
        'body': os.environ['ISSUE_BODY'], 
        'created_at': parse_date(os.environ['ISSUE_CREATED_AT']), # 2023-09-04T15:34:54Z
        'updated_at': parse_date(os.environ['ISSUE_UPDATED_AT']), # 2023-09-04T15:34:54Z
    }

    template_post = dict(**post)
    template_post['date'] = template_post['created_at'].strftime("YYYY-MM-DD HH:MM:SS") # YYYY-MM-DD HH:MM:SS

    print (f"post_id: {post['id']}")
    print (f"post_title: {post['title']}")
    print (f"post_body: {post['body']}")
    print (f"post_created_at: {post['created_at']}")
    print (f"post_updated_at: {post['updated_at']}")

    print (post_template.substitute(**template_post))

if __name__ == "__main__":
    main()
