fn check_wrong(index: usize, nums: &Vec<usize>) -> bool {
    for i in index - 25..nums.len() - 1 {
        for j in i + 1..index {
            if nums[i] + nums[j] == nums[index] {
                return true;
            }
        }
    }
    false
}

fn wrong_index(nums: &Vec<usize>) -> usize {
    for i in 25..nums.len() {
        if !check_wrong(i, &nums) {
            return i;
        }
    }
    panic!("No solution found!");
}

struct SumQueue {
    low: usize,
    high: usize,
    sum: usize,
    vec: Vec<usize>,
}

impl SumQueue {
    fn grow(&mut self, max: usize) {
        while self.sum < max {
            self.high += 1;
            self.sum += self.vec[self.high];
        }
    }
    fn shrink(&mut self, max: usize) {
        while self.sum > max {
            self.sum -= self.vec[self.low];
            self.low += 1;
        }
    }
    fn get_sum(&mut self) -> usize {
        let slice = &mut self.vec[self.low..=self.high];
        slice.sort();
        slice[0] + slice[slice.len() - 1]
    }
}

#[cfg(test)]
mod test {
    use std::fs::read_to_string;

    use super::{wrong_index, SumQueue};

    #[test]
    fn d9p1() {
        // preamble
        let nums: Vec<usize> = read_to_string("res/reddit/d9")
            .unwrap()
            .lines()
            .map(|l| l.parse().unwrap())
            .collect();

        println!("Solution: {}", nums[wrong_index(&nums)]);
    }

    #[test]
    fn d9p2() {
        let nums: Vec<usize> = read_to_string("res/reddit/d9")
            .unwrap()
            .lines()
            .map(|l| l.parse().unwrap())
            .collect();
        let wrong = nums[wrong_index(&nums)];
        let mut queue = SumQueue {
            low: 0,
            high: 1,
            sum: nums[0] + nums[1],
            vec: nums,
        };

        while queue.sum != wrong {
            queue.grow(wrong);
            queue.shrink(wrong);
        }
        println!("Solution: {}", queue.get_sum());
    }
}
