let explode s = List.init (String.length s) (String.get s)

let s = 
  let channel = open_in "input.txt" in
  let length = in_channel_length channel in
  let content = really_input_string channel length in
  close_in channel;
  content

let rec sol s = 
  match s with
  | '('::tl -> 1 + sol(tl)
  | ')'::tl -> -1 + sol(tl)
  | _ -> 0

let () = 
  let res = sol (explode s) in
  print_endline (string_of_int res);