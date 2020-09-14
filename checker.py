import requests
import hashlib
import sys

def req_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+ query_char
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'error fetchin:{res.status_code}, check it again ')
    return res


def get_pass_leak_count(hashes,hashes_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count  in hashes:
        if h == hashes_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password=(hashlib.sha1(password.encode('Utf-8')).hexdigest().upper())       
    first5_char, tail=sha1password[:5],sha1password[5:]
    response=req_api_data(first5_char)
    return get_pass_leak_count(response,tail)

def main(sys):
    for password in sys:
        count=pwned_api_check(password)
        if count:
            print(f' {password} was found {count}, you better change it now')

        else:
            print(f'{password} was not found, you can carry on')

    return "done!"

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))