use std::collections::HashSet;

fn parse_answers(ans: &str) -> usize {
    ans.split_ascii_whitespace()
        .collect::<String>()
        .chars()
        .collect::<HashSet<_>>()
        .len()
}

fn parse_answers2(ans: &str) -> usize {
    let vec: Vec<HashSet<char>> = ans
        .lines()
        .map(|l| l.chars().collect::<HashSet<_>>())
        .collect();

    vec.first()
        .unwrap()
        .into_iter()
        .filter(|c| vec.iter().all(|s| s.contains(c)))
        .count()
}

#[cfg(test)]
mod test {
    use std::fs::read_to_string;

    use super::{parse_answers, parse_answers2};

    #[test]
    fn d6p1() {
        println!(
            "Solution: {}",
            read_to_string("res/reddit/d6")
                .unwrap()
                .split("\n\n")
                .map(|ans| parse_answers(ans))
                .sum::<usize>()
        );
    }

    #[test]
    fn d6p2() {
        println!(
            "Solution: {}",
            read_to_string("res/reddit/d6")
                .unwrap()
                .split("\n\n")
                .map(|ans| parse_answers2(ans))
                .sum::<usize>()
        );
    }
}
