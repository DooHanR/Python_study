""" invoke를 시행해보기 위해 만들어진 파일. """

from invoke import task

@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)

