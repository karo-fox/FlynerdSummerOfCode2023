segments = int(input("Ile segmentów ma mieć choinka?: "))
for seg in range(segments):
    for i in range(1, seg + 3):
        print("#" * i)
