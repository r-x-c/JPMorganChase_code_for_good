//
//  SecondViewController.swift
//  Choices
//
//  Created by Marco Schwiebert on 10/14/16.
//  Copyright © 2016 mschwiebert. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {

    @IBOutlet weak var timelineProgress: UIProgressView!
    @IBOutlet weak var gpaLabel: UILabel!
    @IBOutlet weak var disciplineProgress: UIProgressView!
    @IBOutlet weak var balanceProgress: UIProgressView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    override func viewDidAppear(animated: Bool) {
        
        gpaLabel.text = "GPA: \(gpa)/4.00"
    }

}

