people = ["Luis","Carlos","Myriam","Tatiana","Sofia","Fernando","Sofia"]
more_people = ["Sandra","Sebastian","Jorge","Carolina","Jose","Sofia"]
all_people = people + more_people

print(f"En People hay {len(people)} nombres, desde {min(people)} hasta {max(people)} ")
print(f"En People hay {len(more_people)} nombres, desde {min(more_people)} hasta {max(more_people)} ")

print(f"Unidos son {len(all_people)} nombres, desde {min(all_people)} hasta {max(all_people)} ")

look_for = "Carlos"

print(f"{look_for} figura {all_people.count(look_for)} vez/veces.")

max=0
who=""

for _ in all_people:
    cnt = all_people.count(_)
    who = _
    if  cnt > max:
        max = cnt
        who = _
print(f"{who} está {cnt} veces.")

# s.index(x[, i[, j]])
# index of the first occurrence of x in s
# (at or after index i and before index j)

print(all_people.index(who))
ix=all_people.index(who)
who=all_people[ix+1]
print(who)

print("Orden ascendente ")

for _ in (sorted(all_people, reverse=False)):
    print(f"{_}, ",end="")

print("\nOrden descendente ")

for _ in (sorted(all_people, reverse=True)):
    print(f"{_} ,",end="")
print()