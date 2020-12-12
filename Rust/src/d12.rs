use std::fs::read_to_string;

struct Instruction {
    command: char,
    val: i64,
}
impl From<&str> for Instruction {
    fn from(s: &str) -> Self {
        let command = s.chars().nth(0).unwrap();
        let val = s.split_at(1).1.parse().unwrap();
        Instruction { command, val }
    }
}

fn parse_file() -> Vec<Instruction> {
    read_to_string("res/reddit/d12")
        .unwrap()
        .lines()
        .map(|l| Instruction::from(l))
        .collect()
}

fn set_wp_dir(north: &mut i64, east: &mut i64, i: &Instruction) {
    if (i.val == 90 && i.command == 'R') || (i.val == 270 && i.command == 'L') {
        let tmp = *north;
        *north = -*east;
        *east = tmp;
    } else if i.val == 180 {
        *north = -*north;
        *east = -*east;
    } else if (i.val == 270 && i.command == 'R') || (i.val == 90 && i.command == 'L') {
        let tmp = *north;
        *north = *east;
        *east = -tmp;
    } else {
        panic!("Unexpected value {}", i.val);
    }
}

#[cfg(test)]
mod test {
    use super::{parse_file, set_wp_dir};

    #[test]
    fn d12p1() {
        let instructions = parse_file();
        let mut dir = 0;
        let mut north = 0i64;
        let mut east = 0i64;

        for i in instructions {
            match i.command {
                'N' => north += i.val,
                'E' => east += i.val,
                'S' => north -= i.val,
                'W' => east -= i.val,
                'L' => dir = (dir + 360 - i.val) % 360,
                'R' => dir = (dir + i.val) % 360,
                'F' => match dir {
                    0 => east += i.val,
                    90 => north -= i.val,
                    180 => east -= i.val,
                    270 => north += i.val,
                    _ => panic!("Unexpected value {}", dir),
                },
                _ => panic!("Wrong command!"),
            }
        }

        println!("Solution: {}", north.abs() + east.abs());
    }
    #[test]
    fn d12p2() {
        let instructions: Vec<_> = parse_file();
        let mut north = 0i64;
        let mut east = 0i64;
        let mut wp_north = 1i64;
        let mut wp_east = 10i64;

        for i in instructions {
            match i.command {
                'N' => wp_north += i.val,
                'E' => wp_east += i.val,
                'S' => wp_north -= i.val,
                'W' => wp_east -= i.val,
                'L' | 'R' => set_wp_dir(&mut wp_north, &mut wp_east, &i),
                'F' => {
                    north += i.val * wp_north;
                    east += i.val * wp_east;
                }

                _ => panic!("Wrong command!"),
            }
        }

        println!("Solution: {}", north.abs() + east.abs());
    }
}
