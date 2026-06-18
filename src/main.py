from attendance import summarize_attendance

def main():
    attendance_batches = [
        [True, True, False, True],
        [],
        [True, False, False, True, True]
    ]

    for records in attendance_batches:
        summary = summarize_attendance(records)
        print(summary)

if __name__ == "__main__":
    main()
