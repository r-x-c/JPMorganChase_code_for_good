//
//  RegisterViewController_.swift
//  Choices
//
//  Created by Marco Schwiebert on 10/15/16.
//  Copyright © 2016 mschwiebert. All rights reserved.
//

import UIKit

class RegisterViewController_: UIViewController, UIPickerViewDataSource, UIPickerViewDelegate
 {

    @IBOutlet weak var pickerView: UIPickerView!
    
    var pickerDataSource = [["13", "14", "15", "16", "17", "18"],["Male","Female","Other"],["American Indian","Asian","Black or African American", "Hispanic/Latino", "White", "Other"]]
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    func numberOfComponentsInPickerView(pickerView: UIPickerView) -> Int {
        return pickerDataSource.count
    }
    func pickerView(pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return pickerDataSource[component].count;
    }
    
    func pickerView(pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String! {
        return pickerDataSource[component][row]
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    func pickerView(pickerView: UIPickerView, widthForComponent component: Int) -> CGFloat {
        if component == 0{
            return 50
        } else if component == 1{
            return 85
        } else {return 300}
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
