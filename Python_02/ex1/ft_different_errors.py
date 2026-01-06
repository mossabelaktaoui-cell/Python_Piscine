def garden_operations():
    print("=== Garden Error Types Demo ===\n")
    try:
        input_ =  int(input())
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except KeyError:
        print("Testing KeyError...")
        print("Caught KeyError: 'missing\_plant'")
    except:
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!")
    print("All error types tested successfully!")