def fun(s):
    username = s.partition('@')[0]
    domain = s.partition('@')[2].partition('.')[0]
    ext = s.partition('@')[2].partition('.')[2]
    return ((username.isidentifier() or '-' in username) and domain.isalnum() and ext.isalpha() and len(ext) > 0 and len(ext) <= 3)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)