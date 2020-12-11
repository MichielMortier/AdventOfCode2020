use std::collections::HashMap;

fn find_mut(vec: &Vec<usize>) {
    let mut map = HashMap::new();
    for i in 0..vec.len() {
        let mut j = i + 2;
        let mut skips = Vec::new();
        while j < vec.len() && vec[j] - vec[i] <= 3 {
            skips.push(vec[j - 1]);
            j += 1;
        }
        map.insert(vec[i], skips);
    }

    let mut cumul = HashMap::new();
    cumul.insert(vec.last().unwrap(), 1);

    for i in (0..(vec.len() - 1)).rev() {
        let skips = &map[&vec[i]];
        let mut c: usize = cumul[&vec[i + skips.len() + 1]];
        for j in skips.iter() {
            c += cumul[j];
        }
        cumul.insert(&vec[i], c);
    }

    println!("Solution: {}", cumul[vec.first().unwrap()]);

    println!("{:?}", map);
}

fn find_num_muts(
    mut last: usize,
    mut i: usize,
    vec: &Vec<usize>,
    mut indices: Vec<usize>,
) -> usize {
    let mut count = 1;

    while i < vec.len() {
        if vec[i] - vec[last] <= 3 {
            let mut clone = indices.clone();
            clone.pop();
            count += find_num_muts(last, i + 1, vec, clone);
        }
        last = indices.pop().unwrap();
        i += 1;
    }

    count
}

#[cfg(test)]
mod test {
    use std::{fs::read_to_string, time::Instant};

    use super::{find_mut, find_num_muts};

    #[test]
    fn d10p1() {
        let mut lines: Vec<usize> = read_to_string("res/reddit/d10")
            .unwrap()
            .lines()
            .map(|l| l.parse().unwrap())
            .collect();
        lines.sort();

        let mut count_1 = 1;
        let mut count_3 = 1;

        for i in 1..lines.len() {
            if lines[i] - lines[i - 1] > 1 {
                count_3 += 1;
            } else {
                count_1 += 1;
            }
        }

        println!("Solution: {} {} {}", count_1, count_3, count_1 * count_3);
    }

    #[test]
    fn d10p2() {
        let now = Instant::now();
        let mut lines: Vec<usize> = read_to_string("res/reddit/d10")
            .unwrap()
            .lines()
            .map(|l| l.parse().unwrap())
            .collect();
        lines.sort();
        find_mut(&lines);
        println!("Time passed: {}", now.elapsed().as_micros());
    }
}
