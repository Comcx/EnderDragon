#[derive(Copy, Clone)]
enum Status {
    Todo,
    Work,
    Done,
}

impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let num = num_courses as usize;
        let mut graph = vec![Vec::new(); num];
        for edge in prerequisites.iter() {
            graph[edge[0] as usize].push(edge[1] as usize);
        }
        let mut status = vec![Status::Todo; num];
        (0..num).all(|course| !has_cycle(course, &mut status, &graph))
    }
}

fn has_cycle(course: usize, status: &mut Vec<Status>, graph: &Vec<Vec<usize>>) -> bool {
    match status[course] {
        Status::Done => false,
        Status::Work => true,
        _ => {
            status[course] = Status::Work;
            if graph[course].iter()
                .any(|&next_course| has_cycle(next_course, status, graph))
            {
                return true;
            }
            status[course] = Status::Done;
            false
        }
    }
}
