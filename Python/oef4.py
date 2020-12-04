from file_handler import *
import re

needed = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines_no_strip()
    total = ""
    for line in lines:
        total += line
    lijst = [x.replace("\n", " ") for x in total.split("\n\n")]
    count = 0
    for passport in lijst:
        if all((element in passport) for element in needed):
            count += 1
    print(count)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines_no_strip()
    total = ""
    for line in lines:
        total += line
    lijst = [x.replace("\n", " ") for x in total.split("\n\n")]
    count = 0
    for passport in lijst:
        if all((element in passport) for element in needed):
            result = sorted(passport.split(" "))
            if result[1].startswith("cid"):
                result.remove(result[1])
            byr, ecl, eyr, hcl, hgt, iyr, pid = [x.split(":")[1] for x in result]
            if (1920 <= int(byr) <= 2002
                    and 2010 <= int(iyr) <= 2020 <= int(eyr) <= 2030
                    and ((hgt.endswith("cm") and 150 <= int(hgt.strip("cm")) <= 193) or (
                            hgt.endswith("in") and 59 <= int(hgt.strip("in")) <= 76))
                    and re.match("^#[0-9,a-f]{6}$", hcl)
                    and ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
                    and re.match("^[0-9]{9}$", pid)
            ):
                print(result)
                count += 1
    print(count)
