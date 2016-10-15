//
//  MessageTableViewCell.swift
//  Choices
//
//  Created by Marco Schwiebert on 10/14/16.
//  Copyright © 2016 mschwiebert. All rights reserved.
//

import UIKit

class MessageTableViewCell: UITableViewCell {

    @IBOutlet weak var userName: UILabel!
    @IBOutlet weak var textMessage: UITextView!
    
    @IBOutlet weak var timeStamp: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
