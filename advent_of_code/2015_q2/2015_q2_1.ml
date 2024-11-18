let open_input filename = 
  let channel = open_in filename in
  let rec get_lines acc =
    try 
      let line = input_line channel in
      get_lines (line :: acc)
    with e ->
      List.rev acc
  in get_lines []

let () =
  let lines = open_input "input.txt" in
  let rec sol l =
    match l with 
    | [] -> 0
    | hd::tl -> 
      match (String.split_on_char 'x' hd) with
      | l::w::h::[] -> let l = int_of_string l in 
                   let w = int_of_string w in 
                   let h = int_of_string h in
                   let x = (l*w) in
                   let y = (w*h) in
                   let z = (h*l) in

                   (2*x) + (2*y) + (2*z) + (let m = min x y in min m z) + sol tl
      | _ -> 0
  
    in print_endline (string_of_int (sol lines))