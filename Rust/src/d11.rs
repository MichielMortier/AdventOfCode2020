use core::panic;

#[derive(Debug, PartialEq, Clone)]
enum Seat {
    Floor,
    Taken,
    Empty,
}

impl From<char> for Seat {
    fn from(c: char) -> Self {
        match c {
            'L' => Seat::Empty,
            '#' => Seat::Taken,
            '.' => Seat::Floor,
            _ => panic!("Wrong character!"),
        }
    }
}

fn is_in_range(x: i64, y: i64, seats: &Vec<Vec<Seat>>) -> bool {
    x >= 0 && x < (seats[0].len() as i64) && y >= 0 && y < (seats.len() as i64)
}

fn act(x: usize, y: usize, count: usize, move_when: usize, seats: &mut Vec<Vec<Seat>>) -> bool {
    match &seats[y][x] {
        Seat::Taken if count >= move_when => {
            seats[y][x] = Seat::Empty;
            return true;
        }
        Seat::Empty if count == 0 => {
            seats[y][x] = Seat::Taken;
            return true;
        }
        _ => false,
    }
}

fn switch(x: usize, y: usize, seats: &Vec<Vec<Seat>>, new_seats: &mut Vec<Vec<Seat>>) -> bool {
    let mut count = 0;
    for dx in -1i64..=1i64 {
        for dy in -1i64..=1i64 {
            let xx = x as i64 + dx;
            let yy = y as i64 + dy;
            if is_in_range(xx, yy, seats) && !(dx == 0 && dy == 0) {
                if seats[yy as usize][xx as usize] == Seat::Taken {
                    count += 1;
                }
            }
        }
    }

    act(x, y, count, 4, new_seats)
}

fn switch2(x: usize, y: usize, seats: &Vec<Vec<Seat>>, new_seats: &mut Vec<Vec<Seat>>) -> bool {
    let mut count = 0;
    for dx in -1i64..=1i64 {
        for dy in -1i64..=1i64 {
            let mut i = 1;
            loop {
                let xx = x as i64 + dx * i;
                let yy = y as i64 + dy * i;
                if is_in_range(xx, yy, seats) && !(dx == 0 && dy == 0) {
                    if seats[yy as usize][xx as usize] == Seat::Taken {
                        count += 1;
                        break;
                    }
                    if seats[yy as usize][xx as usize] == Seat::Empty {
                        break;
                    }
                } else {
                    break;
                }
                i += 1;
            }
        }
    }
    act(x, y, count, 5, new_seats)
}

fn step<F>(seats: &mut Vec<Vec<Seat>>, f: F) -> bool
where
    F: Fn(usize, usize, &Vec<Vec<Seat>>, &mut Vec<Vec<Seat>>) -> bool,
{
    let mut changed = false;
    let mut new_seats = seats.clone();
    for y in 0..seats.len() {
        for x in 0..seats[y].len() {
            if f(x, y, seats, &mut new_seats) {
                changed = true;
            }
        }
    }
    *seats = new_seats;
    changed
}
fn count(seats: &Vec<Vec<Seat>>) -> usize {
    seats
        .iter()
        .flat_map(|line| line)
        .filter(|seat| **seat == Seat::Taken)
        .count()
}

#[cfg(test)]
mod test {
    use std::fs::read_to_string;

    use super::{count, step, switch, switch2, Seat};

    #[test]
    fn d11p1() {
        let mut seats: Vec<Vec<_>> = read_to_string("res/reddit/d11")
            .unwrap()
            .lines()
            .map(|l| l.chars().map(|c| Seat::from(c)).collect())
            .collect();

        while step(&mut seats, switch) {}
        println!("Solution: {}", count(&seats));
    }
    #[test]
    fn d11p2() {
        let mut seats: Vec<Vec<_>> = read_to_string("res/reddit/d11")
            .unwrap()
            .lines()
            .map(|l| l.chars().map(|c| Seat::from(c)).collect())
            .collect();

        while step(&mut seats, switch2) {}
        println!("Solution: {}", count(&seats));
    }
}
