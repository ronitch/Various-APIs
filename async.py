import asyncio

async def f1():
    print("f1 started")
    print("Task 1 started")
    print("Task 1 finished")
    task2 = asyncio.create_task(f2())
    """
    A Couroutine is a wrapper around a regular function that lets it run asynchronously.
    Creating a Task for the Couroutine f2, this is telling the Event Loop to run it asap, 
    but only 1 thing can be run at a time, and since main() is running now, this task will 
    only execute when main() is finished or if there is an await.
    """

    #await asyncio.sleep(3)
    """
    Putting this await in main() means that while the main() is paused, the Event Loop will
    execute the Task.
    """

    print("Waiting for f2, but lets finish the next task")
    #print("Not waiting for f2, so lets finish the next task")
    print("Task 3 which is independent of task2 started")
    print("Task 3 finished")
    print("Task 4 started, but its dependent on task 2")
    await task2
    """
    If an await task is put, then it'll wait for the task to finish, even if there's a longer
    await in the task.
    """
    print("Task 4 finished")
    print("Task 5 started")
    print("Task 5 finished")
    print("f1 finished")

async def f2():
    print("Task 2  started")
    await asyncio.sleep(5)
    """
    If an await is put in this Task, then when the event loop gives the control from main() to
    f2(), upon encountering this await, the control will go back to main() and the await there
     will be evaluated again. If no await is put, then this task will be completed.
    """

    print("Task 2 finished")

asyncio.run(f1())
print("everything done")