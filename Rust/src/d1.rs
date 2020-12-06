#[cfg(test)]
mod test {
    use crate::_read_number_file;

    #[test]
    fn d1p1() {
        let nums = _read_number_file("res/reddit/d1");
        for i in 0..nums.len() - 1 {
            for j in i + 1..nums.len() {
                if nums[i] + nums[j] == 2020 {
                    println!("Result: {}", nums[i] * nums[j]);
                }
            }
        }
    }

    #[test]
    fn d1p2() {
        let nums = _read_number_file("res/reddit/d1");
        for i in 0..nums.len() - 2 {
            for j in i + 1..nums.len() - 1 {
                for k in j + 1..nums.len() {
                    if nums[i] + nums[j] + nums[k] == 2020 {
                        println!("Result: {}", nums[i] * nums[j] * nums[k]);
                    }
                }
            }
        }
    }
}
