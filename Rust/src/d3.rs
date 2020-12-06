#[cfg(test)]
mod test {
    use std::fs::read_to_string;

    type Matrix = Vec<Vec<char>>;

    fn _next_pos1(
        x: usize,
        y: usize,
        slope_x: usize,
        slope_y: usize,
        matrix: &Matrix,
    ) -> (usize, usize, char) {
        let new_x = (x + slope_x) % matrix[y].len();
        let new_y = y + slope_y;
        let character = match new_y {
            t if t >= matrix.len() => 'S',
            _ => matrix[new_y][new_x],
        };

        (new_x, new_y, character)
    }

    fn find_trees(slope_x: usize, slope_y: usize, matrix: &Matrix) -> usize {
        let mut counter = 0;
        let mut state = (0, 0, 'N');

        state = _next_pos1(state.0, state.1, slope_x, slope_y, &matrix);
        while state.2 != 'S' {
            if state.2 == '#' {
                counter += 1;
            }
            state = _next_pos1(state.0, state.1, slope_x, slope_y, &matrix);
        }

        counter
    }

    #[test]
    fn d3p1() {
        let matrix: Matrix = read_to_string("res/reddit/d3")
            .unwrap()
            .lines()
            .map(|l| l.chars().collect())
            .collect();

        println!(
            "Solution: {}",
            vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
                .iter()
                .fold(1, |acc, e| acc * find_trees(e.0, e.1, &matrix))
        );
    }
}
