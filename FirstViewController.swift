//
//  FirstViewController.swift
//  Choices
//
//  Created by Marco Schwiebert on 10/14/16.
//  Copyright © 2016 mschwiebert. All rights reserved.
//

import UIKit

var gpa = 3.51


class FirstViewController: UIViewController, UITableViewDelegate {
    
    //for the demo
    var questions = ["Hey did you hear about the party tonight? Forget your homework tonight, we have to go. So I'll meet you there at 9?",
                     "Hey I heard the bully is going to try to corner you after school. What are you gonna do?"]
    var answers = [["I think I'm gonna stay in tonight, I can't blow off this much work.",
                    "I'm not feeling the party but let's chill tonight.",
                    "I was just about to ask you the same thing, let's do it.",
                    "I've been coding for literally 24 hours, I can't handle a party right now."],
                   ["Fight back obviously, I can take them!",
                    "I'm gonna just take the long way home. No point in conflict.",
                    "I'll just head home with my friends, no way he starts something with them around.",
                    "I'll corner him first and take the fight to him."]]
    var timeStamps = ["8:00 PM", "8:03 PM", "11:00 AM", "11:30 AM","8:00 PM", "8:03 PM", "11:00 AM", "11:30 AM"]
    var demo_stage = 0 //out of 4 stages

    
    var ans = [1]
    
    //the different choice scenarios:
    
    @IBOutlet weak var option1text: UITextView!
    
    @IBOutlet weak var option2text: UITextView!
    
    @IBOutlet weak var option3text: UITextView!
    
    @IBOutlet weak var option4text: UITextView!
    
    
    
    
    @IBOutlet weak var messagesTableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        option1text.text = answers[demo_stage][0]
        option2text.text = answers[demo_stage][1]
        option3text.text = answers[demo_stage][2]
        option4text.text = answers[demo_stage][3]

        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    func numberOfSectionsInTableView(tableView: UITableView) -> Int{
        return 1
    }
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int{
        return demo_stage*2 + 1
    }
    let NUM_CYCLES = 2
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell{
        let cell = tableView.dequeueReusableCellWithIdentifier("Cell", forIndexPath: indexPath) as! MessageTableViewCell
        if indexPath.row % 2 == 0{
            cell.textMessage.text = questions[indexPath.row % NUM_CYCLES]
            cell.timeStamp.text = timeStamps[indexPath.row % 7]
            cell.userName.text = "Richard"
        } else {
            print("in else")
            cell.textMessage.text = answers[indexPath.row % NUM_CYCLES][ans[indexPath.row % NUM_CYCLES]]
            cell.timeStamp.text = timeStamps[indexPath.row % 7]
            cell.userName.text = "Brent"
            
        }

        
        return cell
    }

    
    @IBAction func option1(sender: AnyObject) {
        ans.append(0)
        demo_stage+=1
        messagesTableView.reloadData()
        option1text.text = answers[demo_stage % NUM_CYCLES][0]
        option2text.text = answers[demo_stage % NUM_CYCLES][1]
        option3text.text = answers[demo_stage % NUM_CYCLES][2]
        option4text.text = answers[demo_stage % NUM_CYCLES][3]
        print("option1")
        gpa += 0.03
        
    }
    @IBAction func option2(sender: AnyObject) {
        ans.append(1)
        demo_stage+=1
        messagesTableView.reloadData()
        option1text.text = answers[demo_stage % NUM_CYCLES][0]
        option2text.text = answers[demo_stage % NUM_CYCLES][1]
        option3text.text = answers[demo_stage % NUM_CYCLES][2]
        option4text.text = answers[demo_stage % NUM_CYCLES][3]
        print("option2")
        gpa += -0.05
    }
    
    @IBAction func option3(sender: AnyObject) {
        ans.append(2)
        demo_stage+=1
        messagesTableView.reloadData()
        option1text.text = answers[demo_stage % NUM_CYCLES][0]
        option2text.text = answers[demo_stage % NUM_CYCLES][1]
        option3text.text = answers[demo_stage % NUM_CYCLES][2]
        option4text.text = answers[demo_stage % NUM_CYCLES][3]
        print("option3")
        gpa += -0.07
        
    }
    @IBAction func option4(sender: AnyObject) {
        ans.append(3)
        demo_stage+=1
        messagesTableView.reloadData()
        option1text.text = answers[demo_stage % NUM_CYCLES][0]
        option2text.text = answers[demo_stage % NUM_CYCLES][1]
        option3text.text = answers[demo_stage % NUM_CYCLES][2]
        option4text.text = answers[demo_stage % NUM_CYCLES][3]
        print("option4")
        gpa += 0.1
    }
}

