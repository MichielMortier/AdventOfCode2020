fn bin_search(low: u64, high: u64, left: bool) -> (u64, u64) {
    let pos = low + (high - low) / 2;
    match left {
        true => (low, pos),
        false => (pos, high),
    }
}

fn find_row(ticket: &str) -> u64 {
    ticket
        .chars()
        .take(7)
        .map(|c| c == 'F')
        .fold((0, 127), |init, val| bin_search(init.0, init.1, val))
        .1
}

fn find_col(ticket: &str) -> u64 {
    ticket
        .chars()
        .skip(7)
        .map(|c| c == 'L')
        .fold((0, 7), |init, val| bin_search(init.0, init.1, val))
        .1
}

#[cfg(test)]
mod test {
    use std::{collections::HashSet, fs::read_to_string};

    use super::find_col;
    use super::find_row;

    #[test]
    fn d5p1() {
        println!(
            "Solution: {}",
            read_to_string("res/reddit/d5")
                .unwrap()
                .lines()
                .map(|l| find_row(l) * 8 + find_col(l))
                .max()
                .unwrap()
        );
    }
    #[test]
    fn d5p2() {
        let set: HashSet<u64> = read_to_string("res/reddit/d5")
            .unwrap()
            .lines()
            .map(|l| find_row(l) * 8 + find_col(l))
            .collect();

        println!(
            "Solution: {}",
            (0..=1024)
                .skip_while(|i| !set.contains(i))
                .find(|i| !set.contains(i))
                .unwrap()
        );
    }
}
